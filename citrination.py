#!/usr/bin/env python

import upload
import create_dataset
import create_dataset_version
import command_router

app = command_router.CommandRouter()
app.register(upload.App, ['upload'])
app.register(create_dataset.App, ['create_dataset'])
app.register(create_dataset_version.App, ['create_dataset_version'])

if __name__ == "__main__":
    app.run()
