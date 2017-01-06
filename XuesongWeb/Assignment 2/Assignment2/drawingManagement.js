// The following prototype is defined to store drawing information.
function Drawing(id,bn,year,con,floor)
{
    this.DrawingID = id;
    this.BuildingName = bn;
    this.ConstructedYear = year;
    this.Contractor = con;
    this.Floor = floor;
}


// The following statement does not belong to any method. Hence,
// it is a global variable that can be accessed by any methods in this
// webpage.
// This global variable is an array that will be used to store objects
// of the drawing information.
var drawings = [];

// The following statement is a method that create initial drawing objects
// and add them to the array drawings.
function initDrawings()
{
    // Empty the array first.
    drawings = [];
    // In order to create a new object, we use the new keyword with the prototype name.
    var newDrawing = new Drawing("Port_001", "Porter Hall",2009,"PJ Dick",1);
    drawings.push(newDrawing);

    newDrawing = new Drawing("Port_002", "Porter Hall",2009,"PJ Dick",2);
    drawings.push(newDrawing);
    newDrawing = new Drawing("Wean_001", "Wean Hall",1998,"Jendoco",4);
    drawings.push(newDrawing);
    newDrawing = new Drawing("Wean_002", "Wean Hall",1998,"Trane",6);
    drawings.push(newDrawing);

    // Task 1.b, please add a new attribute, Shop, to the prototype Drawing,
    // and then add two new drawing objects.
    newDrawing = new Drawing("NSH_001", "Newell Simon Hall", 1988, "Turner", 3);
    newDrawing.Shop = "Architecture";
    drawings.push(newDrawing);
    newDrawing = new Drawing("NSH_002", "Newell Simon Hall", 1988, "Turner", 2);
    newDrawing.Shop = "Structure";
    drawings.push(newDrawing);



}

// The following method load drawing data to create drawing objects,
// and then add the ID of the objects to the dropdown list, with the ID
// DrawingIDList.
function addDrawingInfoToList()
{
    if(drawings.length==0)
    {
        alert("Please load the initial drawings to the array first.");
        return;
    }

    // First, we need to get a reference of the HTML tag DrawingIDList.
    var HTMLDrawingList = document.getElementById("DrawingIDList");

    // Before adding all drawings to the list, the list needs to be
    // emptied so that no repeated item will show.
    // One simple way to empty a list is to set innerHTML of the list
    // to an empty string, which means that there is no option tag.
    HTMLDrawingList.innerHTML = "";

    // Now we can started to add new items to the list.
    for(var i=0;i<drawings.length;i++)
    {
        // Get the reference of the current drawing in the loop.
        var drawing = drawings[i];

        // In order to add an item to the list, we need to create a
        // tag <option>, which defines an item in a <select> tag.
        var newOption = document.createElement("option");
        
        // Then provide the innerText to this option.
        
        // Task 1.c, assign the attribute DrawingID of the current drawing
        // to the inner text of the created option tag.
        newOption.text = drawing.DrawingID;
        
        // Now we can add the new <option> tag to the <select> tag to
        // show the new item.
        HTMLDrawingList.appendChild(newOption);
    }

    alert("A total of "+drawings.length+" drawings are added to the HTML list.");

}

// The following event is triggered by the change of selection in the drawing
// information list.
function drawingInfoListChange()
{
    var HTMLDrawingList = document.getElementById("DrawingIDList");

    // The selectedIndex attribute belongs to any <select> tag.
    // It represents the current index of the selected item.
    var drawingIndex = HTMLDrawingList.selectedIndex;

    // Since the items in the drawinginfoList is the same order
    // as the drawings list, the index of the selected item also represents
    // the index of the drawing item in the array.
    var selectedDrawing = drawings[drawingIndex];

    // Now we can use this selected object of the drawing to update the
    // drawing information.

    // Task 1.d, please use the information in selectedDrawing to finish the 
    // five <input> tags.
    var buildingName = document.getElementById("buildingNameInput");
    var constructionYear = document.getElementById("constructedYearInput");
    var contractor = document.getElementById("contractorInput");
    var floor = document.getElementById("floorInput");
    var shop = document.getElementById("shopInput");

    buildingName.value = selectedDrawing.BuildingName;
    constructionYear.value = selectedDrawing.ConstructedYear;
    contractor.value = selectedDrawing.Contractor;
    floor.value = selectedDrawing.Floor;
    shop.value = selectedDrawing.Shop;

}

function hasIdInDrawings(newId) {
    for (var i = 0; i < drawings.length;i++) {
        if (drawings[i].DrawingID == newId) {
            return true;
        }
    }
    return false;
}

// The following function asks for a new ID that user will input for the drawing.
// It will check whether there is any drawing that has the same ID. If yes, it will
// provide a message saying that this ID exist. Otherwise, it will add a new drawing object.
// with information in the input boxes to the array and reload the ID to the drawinglist.
function addDrawing()
{
    // Ask the user to enter an ID for the new drawing.
    // Task 1.e, please add the codes to finish the steps described in the assignment.

    // If this ID does not exist, using the information from the current text boxes
    // to create the new drawing object.
    var buildingNameText = document.getElementById("buildingNameInput").value;
    var constructedYearText = document.getElementById("constructedYearInput").value;
    var contractorText = document.getElementById("contractorInput").value;
    var floorText = document.getElementById("floorInput").value;
    var shopText = document.getElementById("shopInput").value;

    var newID;
    var isValidInput = false;
    while(!isValidInput) {
        newID = prompt("Please enter a new ID for the drawing");
        if (newID == null) {
            alert("Please enter the new ID");
        } else {
            isValidInput = !hasIdInDrawings(newID);
        }
    }

    var newDrawing = new Drawing(newID, buildingNameText,constructedYearText,
        contractorText,floorText);

    // Since the attribute Shop does not exist in the cosntructor method, we need to
    // assign its value separately.
    newDrawing.Shop = shopText;

    // Add teh new drawing object to the list.
    drawings.push(newDrawing);

    // Reload the HTML drawing list tag.
    addDrawingInfoToList();
}

// The following function will update the drawing that is currently selected in the 
// HTML drawing list (the <select> tag), using the information in the text boxes.
function updateDrawing()
{
    // First, we need to get the selected index in the HTML drawing list.
    var HTMLDrawingList = document.getElementById("DrawingIDList");
    // The selectedIndex attribute belongs to any <select> tag.
    // It represents the current index of the selected item.
    var drawingIndex = HTMLDrawingList.selectedIndex;

    // Since the items in the drawinginfoList is the same order
    // as the drawings list, the index of the selected item also represents
    // the index of the drawing item in the array.
    var selectedDrawing = drawings[drawingIndex];

    // Task 1.f, please complete the code that update the attributes of selectedDrawing
    // using the five <input> tags.
    var drawingID = selectedDrawing.DrawingID;
    var buildingName = document.getElementById("buildingNameInput").value;
    var constructedYearText = document.getElementById("constructedYearInput").value;
    var contractor = document.getElementById("contractorInput").value;
    var floor = document.getElementById("floorInput").value;
    var shop = document.getElementById("shopInput").value;

    var newDrawing = new Drawing(drawingID, buildingName,constructedYearText,contractor,floor);
    newDrawing.Shop = shop;

    drawings.splice(drawingIndex, 1, newDrawing);

}

// This function is triggered by the button Delete. It will delete the currently
// selected drawing.
function deteleDrawing()
{
    // First, confirm with the user that you are going to delete the selected drawing.
    if(confirm("Are you sure to delete this object?"))
    {
        // Task 1.g, please complete the code to delete the currently selected drawing object.
        var HTMLDrawingList = document.getElementById("DrawingIDList");
        // The selectedIndex attribute belongs to any <select> tag.
        // It represents the current index of the selected item.
        var drawingIndex = HTMLDrawingList.selectedIndex;

        // Since the items in the drawinginfoList is the same order
        // as the drawings list, the index of the selected item also represents
        // the index of the drawing item in the array.
        var selectedDrawing = drawings[drawingIndex];
        drawings.splice(drawingIndex,1);

        // After deleting this object, reload the drawing list.
        addDrawingInfoToList();
    }
}