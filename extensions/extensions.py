# take user input
user_input = input("File name: ")


extensions = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
    "default": "application/octet-stream"
}



if "." in user_input:
    file_name = user_input.strip().split(".")
    extension = file_name[-1]

    if extension.lower() in extensions:
        print(extensions[extension.lower()])
    else:
        print(extensions["default"])
else:
    print(extensions["default"])

