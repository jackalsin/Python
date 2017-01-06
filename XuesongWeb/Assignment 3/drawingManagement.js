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


    // Add a new attribute to the prototype Drawing.
    Drawing.prototype.Shop = "";

    // If the constructor method is changed, the shop attribute can be direclty added when 
    // creating the objects.
    newDrawing = new Drawing("NSH_001", "Newell Simon Hall",1988,"Turner",3);
    newDrawing.Shop = "Architecture";

    drawings.push(newDrawing);
    newDrawing = new Drawing("NSH_002", "Newell Simon Hall",1988,"Turner",2);
    newDrawing.Shop = "Structure";
    drawings.push(newDrawing);


    alert("A total of "+drawings.length+" drawings are added to the array.");

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
    var HTMLDrawingList = $("#DrawingIDList");
    // Before adding all drawings to the list, the list needs to be
    // emptied so that no repeated item will show.
    // One simple way to empty a list is to set innerHTML of the list
    // to an empty string, which means that there is no option tag.
    HTMLDrawingList[0].innerHTML = "";

    // Now we can started to add new items to the list.
    for(var i=0;i<drawings.length;i++)
    {
        // In order to add an item to the list, we need to create a
        // tag <option>, which defines an item in a <select> tag.
        // var newOption = document.createElement("option");
        var newOption = $("<option></option>");

        // Then provide the innerText to this option.
        newOption.text(drawings[i].DrawingID);

        // Every option also has an attribute named value. This attribute
        // can be specified as any values. Here we use the index of the item
        // as the value for each option. But this example does not use the value
        // of options.
        newOption.val(i);

        HTMLDrawingList.append(newOption);
    }

    alert("A total of "+drawings.length+" drawings are added to the HTML list.");
    drawingInfoListChange();
}

// The following event is triggered by the change of selection in the drawing
// information list.
function drawingInfoListChange()
{
    var HTMLDrawingList = $("#DrawingIDList")[0];

    // The selectedIndex attribute belongs to any <select> tag.
    // It represents the current index of the selected item.
    var drawingIndex = HTMLDrawingList.selectedIndex;
    // Since the items in the drawinginfoList is the same order
    // as the drawings list, the index of the selected item also represents
    // the index of the drawing item in the array.
    var selectedDrawing = drawings[drawingIndex];
    // Now we can use this selected object of the drawing to update the
    // drawing information.
    var buildingNameText = $("#buildingNameInput");
    buildingNameText.val(selectedDrawing.BuildingName);

    $("#constructedYearInput").val(selectedDrawing.ConstructedYear);
    $("#contractorInput").val(selectedDrawing.Contractor);
    $("#floorInput").val(selectedDrawing.Floor);

    if(selectedDrawing.Shop != undefined)
        $("#shopInput").val(selectedDrawing.Shop);
    else
       $("#shopInput").val("");

}

// The following function asks for a new ID that user will input for the drawing.
// It will check whether there is any drawing that has the same ID. If yes, it will
// provide a message saying that this ID exist. Otherwise, it will add a new drawing object.
// with information in the input boxes to the array and reload the ID to the drawinglist.
function addDrawing()
{
    // Ask the user to enter an ID for the new drawing.
    var newID = prompt("Please enter a new ID for the drawing");
    if(newID==undefined)
    {
        alert("Please enter the new ID.");
        return;
    }

    // Check whether this new ID exists in the drawing list.
    for(var i=0;i<drawings.length;i++)
    {
        if(drawings[i].DrawingID == newID)
        {
            alert("This ID exists.");
            return;
        }
    }

    // If this ID does not exist, using the information from the current text boxes
    // to create the new drawing object.
    var buildingNameText = $("#buildingNameInput").val();
    var constructedYearText = $("#constructedYearInput").val();
    var contractorText = $("#contractorInput").val();
    var floorText = $("#floorInput").val();
    var shopText = $("#shopInput").val();

    var newDrawing = new Drawing(newID, buildingNameText,constructedYearText,
        contractorText,floorText);

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
    var HTMLDrawingList = $("#DrawingIDList")[0];
    // The selectedIndex attribute belongs to any <select> tag.
    // It represents the current index of the selected item.
    var drawingIndex = HTMLDrawingList.selectedIndex;

    // Since the items in the drawinginfoList is the same order
    // as the drawings list, the index of the selected item also represents
    // the index of the drawing item in the array.
    var selectedDrawing = drawings[drawingIndex];
    selectedDrawing.BuildingName = $("#buildingNameInput").val();
    selectedDrawing.ConstructedYear = $("#constructedYearInput").val();
    selectedDrawing.Contractor = $("#contractorInput").val();
    selectedDrawing.Floor = $("#floorInput").val();
    selectedDrawing.Shop = $("#shopInput").val();

    // After updating the attributes, set the object back to the same location in the drawing array.
    drawings[drawingIndex] = selectedDrawing;
}

function deleteDrawing()
{
    var HTMLDrawingList = $("#DrawingIDList")[0];

    // The selectedIndex attribute belongs to any <select> tag.
    // It represents the current index of the selected item.
    var drawingIndex = HTMLDrawingList.selectedIndex;
    // Delete this item from the array drawings. The splice method can remove the item in an array.
    drawings.splice(drawingIndex,1);
    // After removing this item, reload the data.
    addDrawingInfoToList();

    drawingInfoListChange();

}

$(document).ready(function() {
    $("#addButton").on("click", addDrawing);
    $("#addUpdate").on("click", updateDrawing);
    $("#addDelete").on("click", deleteDrawing);
});