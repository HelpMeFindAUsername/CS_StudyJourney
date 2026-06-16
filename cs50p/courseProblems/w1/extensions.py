file = input("File name: ").lower().strip()

fileName, fileExt = file.split(".")

match fileExt:
    case "gif":
        print("image/gifimage/gif")
    case "jpg":
        print("image/jpeg")
    case "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")

