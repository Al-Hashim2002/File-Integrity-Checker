Python File Integrity Checker

A beginner cybersecurity project that uses SHA-256 hashing to detect changes to files.

Project Overview

This tool calculates a file’s SHA-256 hash and compares it with a previously saved baseline. If the file contents change, the hash comparison can identify the modification.

Objectives

* Understand file integrity and cryptographic hashing.
* Generate SHA-256 hashes using Python.
* Create and store a reference hash.
* Detect file modifications through hash comparison.

Technologies Used

* Python 3
* hashlib
* File handling
* SHA-256
* Windows / Python development environment

Features

* Generate SHA-256 hashes.
* Create a baseline hash.
* Compare the current hash with the baseline.
* Display whether a modification was detected.
* Handle missing files.

How to Run

1. Install Python 3 if it is not already installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:python integrity_checker.py
5. Follow the menu instructions to create a baseline and check the file.

Testing

The project was tested in three scenarios:

1. Create a baseline for the test file.
2. Check the unchanged file and confirm the hashes match.
3. Modify the file and confirm that the checker reports a mismatch.

See the screenshots folder for evidence of the tests.

##Screenshots

### 1. Basline Creation
![alt text](<Screenshot 2026-10-09 105958.png>)

### 2.Successful Integrity Check
![alt text](<Screenshot 2026-10-09 110011.png>)

### 3.File Modification Detected
![alt text](<Screenshot 2026-10-09 110029.png>)

Security Limitations

This is an educational demonstration. A hash comparison detects differences, but does not prove that a file was changed maliciously. If an attacker can modify both the file and its stored baseline, they may be able to hide the change. For stronger protection, baseline hashes should be stored in a trusted, separately protected location.

Author:Hashim Alshareef

Cybersecurity student — beginner Python security project.
