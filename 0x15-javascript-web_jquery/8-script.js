$(document).ready(function() {
  $('#list_movies').click(function() {
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
      const movies = data.results;
      const listElement = $('#list_movies');

      // Clear existing list items
      listElement.empty();

      // Iterate through movies and append titles to the list
      movies.forEach(function(movie) {
        $('<li>').text(movie.title).appendTo(listElement);
      });
    });
  });
});
