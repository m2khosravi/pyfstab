# PyFstab Generator

PyFstab Generator is a small Python script to write and generate /etc/fstab files based on yaml file on Unix-like systems.

NOTE : This script has been designed to configure fstab from scratch only based on YAML so make sure all entry points are included in YAML .

### How To Use This

- Make sure Python is installed on your system.
- install dependencies package.
- run script with sudo privileges user.
- priority and attribute should be Observed like sample yaml structure.
- Root-reserve Option Run **tune2fs** **command** to enable ext4 feature on Disk partition, you can disable it by removing this tag on the YAML file.
- Dump and Pass Options are **disabled** by default (0).

### Usage

1. Run `git clone https://github.com/m2khosravi/pyfstab.git` 
2. Run `pip install -r requirements.txt` to install dependencies
3. Run `python fstab.py samplemountpoints.yml`
4. check out the /etc/fstab and if everything is right use `mount -a` or Restore a backup file if something is wrong.

### Bug Report

- Send any issues to GitHub's issue tracker.
- For feature requests open a [new issue](https://github.com/digitalsurvival/pyfstab/issues/new) with the label "feature request."

### Contribute

If you have a suggestion that would make this better, please fork the repo and create a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/nicefeature`)
3. Commit your Changes (`git commit -m 'ADD nice feature'`)
4. Push to the Branch (`git push origin feature/nicefeature`)
5. Open a Pull Request

Thanks.
