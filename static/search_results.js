$(document).ready(function () {
  // $("#search-query").empty();
  // $("#search-query").append(
  //   '<h2>Search results for "' + searchTerm + '":</h2>'
  // );

  if (result.length === 0) {
    $("#search-results").empty().append("<li>No results found</li>");
  } else {
    display_search_result(result); // Pass the entire result object
  }

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
});
