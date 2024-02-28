$(document).ready(function () {
  var skaterIndexes = [1, 3, 5]; // Example indexes

  // Populate skater names based on the preset indexes
  skaterIndexes.forEach(function (index) {
    var name = names[index];
    if (name) {
      var link = $("<a>")
        .attr("href", "/view/" + index)
        .text(name);
      // Append the link to the search results list
      $("#skater-list").append($("<li>").append(link));
    }
  });
});
