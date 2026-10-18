name: Build Flet APK Definitivo

on:
  push:
    branches: [ main, master ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v4

    - name: Set up Python 3.10
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Set up Java 17
      uses: actions/setup-java@v4
      with:
        distribution: 'temurin'
        java-version: '17'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install --upgrade flet

    - name: Build Android APK
      run: |
        flet build apk --yes

    - name: Upload APK Artifact
      uses: actions/upload-artifact@v4
      with:
        name: Grimorio-v2.0-APK
        path: build/apk/*.apk
