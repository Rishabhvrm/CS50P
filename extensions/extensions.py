# take user input
user_input = input("File name: ")

# create dictionary containing mapping of extension and MIME type
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

# condition for inputs without and extension
# input must contain a dot (.)
if "." in user_input:
    

# print default if file name doesn't have dot(.)
else:
    print(extensions["default"])

