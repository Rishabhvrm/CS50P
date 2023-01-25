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

# condition to check if input has dot(.)
# input must contain a dot (.)
if "." not in user_input:
    # print default if file name doesn't have dot(.)
    print(extensions["default"])

else:
    # split on basis of dot(.)
    file_name = user_input.strip().split(".")
    # pick last element, this should be extension of file
    extension = file_name[-1]

    # check if extension exists in the extensions dictionary
    if extension.lower() in extensions:
        print(extensions[extension.lower()])
    else:
        # print default if extension doesn't exist
        print(extensions["default"])

