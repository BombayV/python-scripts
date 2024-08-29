import glob, os

ID = "id="
NAME = "&name="
SECTIONS = "&sections="
COVER = "&cover="
LINKTO = "&linkTo=true"

coverNames = ["cover=true", "cov", "cover"]
hoverNames = ["cover=false", "hov", "hover"]
fileList = ""

with open("fileList.txt", "r") as file:
  fileList = file.read().splitlines()

def handleFiles():
    targetExtension = input("Enter the target extension (webp, jpg, png, jpeg): ")
    newId = input("Enter an id for the images (ex. sarah-lynn): ")
    newId  = ID + newId
    newName = input("Enter a name for the images (ex. Sarah Lynn): ").replace(" ", "+")
    newName = NAME + newName
    newSections = input("Enter the sections (ex. concerts, portraits): ").replace(",", "+").replace(" ", "")
    newSections = SECTIONS + newSections
    sourceFileName = f"{newId}{newName}{newSections}{COVER}"
    otherFileName = f"{newId}{newName}{newSections}{LINKTO}"

    allImages = glob.glob(f"./sourceImages/*.{targetExtension}")
    currentNum = 0
    for image in allImages:
        if any(name in image for name in coverNames):
            os.rename(image, "./newImages/" + sourceFileName + "true" + '.' + targetExtension)
            fileList.append(sourceFileName + "true" + '.' + targetExtension)
        elif any(name in image for name in hoverNames):
            os.rename(image, "./newImages/" + sourceFileName + "false" + '.' + targetExtension)
            fileList.append(sourceFileName + "false" + '.' + targetExtension)
        else:
            os.rename(image, "./newImages/" + otherFileName + str(currentNum) + '.' + targetExtension)
            fileList.append(otherFileName + str(currentNum) + '.' + targetExtension)
        currentNum += 1
    print("FINISHED!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    handleFiles()
