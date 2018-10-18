# workiva-deploy-tools
workiva-deploy-tools comprises a collection of Python modules for automating manual tasks in Workiva Deploy.

## Installation

### Install requirements:

```bash
pip install -r requirements.txt
```

### Create `settings.py`:

In order to use the scripts contained in this repository you will need to create `settings.py`:

`settings.py`

```python
EMAIL_ADDRESS = '<first.last@workiva.com>'
SMITHY_API_TOKEN = '<token>'
COOKIE_LOCAL = '<first.last@workiva.com:True>'
COOKIE_STAGING = '<SACSID>'
```

## Commands

### rmconsole

```bash
python rmconsole/test_rmconsole_api.py --help
```

### smithy

```bash
python smithy/get_latest_build_id.py --help
```
