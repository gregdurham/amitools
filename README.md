amitools
========================

This aws client currently allows you to pull aws for a specific instance ID for a tag. 

To get the current instance-id: 

`curl http://169.254.169.254/latest/meta-data/instance-id`

If run from the source project:
`amitools --instance i-123456 --tag Name`

Possible options:
```
--instance: Instance ID to collect information from
--tag: Value to return for key
```

Building
========================
`python setup.py build sdist`