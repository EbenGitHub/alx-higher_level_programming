$.get("https://swapi-api.hbtn.io/api/films/?format=json", function(data) {
	movieTitleLists = data.results.map(movie => `<li>${movie.title}</li>`);
	for (let i = 0; i < movieTitleLists.length; i++) {
		$("UL#list_movies").append(movieTitleLists[i]);
	}
});
