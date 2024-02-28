$(document).ready(function () {
  $("#search-bar").on("submit", function (event) {
    event.preventDefault();
    var searchTerm = $("#search-input").val().trim(); // Remove leading and trailing whitespace
    console.log(searchTerm);

    // Check if the search term is empty after trimming whitespace
    if (searchTerm === "") {
      // Clear whitespace from search bar
      $("#search-input").val("");
      // Set focus to search bar
      $("#search-input").focus();
      //   console.log("yippee");
      return; // Exit the function without performing the search
    }

    $.ajax({
      type: "POST",
      url: "/lookup",
      dataType: "json",
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify(searchTerm),
      success: function (result) {
        $("#search-query").empty();
        $("#search-query").append(
          '<h2>Search results for "' + searchTerm + '":</h2>'
        );

        if (result.length === 0) {
          $("#search-results").empty().append("<li>No results found</li>");
        } else {
          display_search_result(result); // Pass the entire result object
        }

        $("#search-input").val("");
        $("#clientInput").focus(); // Set focus to client input
      },
      error: function (request, status, error) {
        console.log("Error");
        console.log(request);
        console.log(status);
        console.log(error);
      },
    });
  });

  function display_search_result(result) {
    $("#search-results").empty(); // Clear previous results
    result.forEach(function (skater) {
      // Generate the link dynamically for each search result
      var link = $("<a>")
        .attr("href", "/view/" + skater.id)
        .text(skater.name);
      // Append the link to the search results list
      $("#search-results").append($("<li>").append(link));
    });
  }

  $("#searchbtn").on("click", function (event) {
    event.preventDefault();
    $("#search-bar").trigger("submit");
  });

  $("#search-bar").keypress(function (event) {
    // Check if the pressed key is "Enter"
    if (event.which === 13) {
      event.preventDefault();
      // Trigger click event on submit button
      $("#search-bar").trigger("submit");
    }
  });
});
