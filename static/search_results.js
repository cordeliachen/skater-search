$(document).ready(function () {
  function highlightPartialWords(searchTerm, text) {
    const escapedTerm = searchTerm.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    const regex = new RegExp(escapedTerm, "gi");
    const highlightedText = text.replace(
      regex,
      (match) => `<span class="accent white-txt">${match}</span>`
    );
    return highlightedText;
  }

  // Function to highlight partial words in skater information
  function highlightSkaterInfo(searchTerm) {
    const skaterTitles = document.querySelectorAll(".card-title");
    const skaterTexts = document.querySelectorAll(".card-text");

    skaterTitles.forEach((title) => {
      const originalText = title.textContent;
      title.innerHTML = highlightPartialWords(searchTerm, originalText);
    });

    skaterTexts.forEach((text) => {
      const originalText = text.textContent;
      text.innerHTML = highlightPartialWords(searchTerm, originalText);
    });
  }

  // Call the highlightSkaterInfo function with the searchTerm provided

  highlightSkaterInfo(searchTerm);
});
