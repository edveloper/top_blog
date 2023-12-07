// Function to toggle the 'active' class for mobile navigation
function toggleMobileNav() {
    const navbarNav = document.getElementById('navbarNav');
    if (navbarNav.classList.contains('show')) {
        navbarNav.classList.remove('show');
    } else {
        navbarNav.classList.add('show');
    }
}

// Function to handle live search
function liveSearch() {
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');

    searchInput.addEventListener('input', function () {
        const query = searchInput.value.trim();

        // Make an AJAX request to the Django view for live search
        fetch(`/search/?q=${query}`)
            .then(response => response.json())
            .then(data => {
                // Clear previous results
                searchResults.innerHTML = '';

                // Display search results as clickable links
                data.forEach(result => {
                    const link = document.createElement('a');
                    link.href = result.url; // URL to the article detail page
                    link.textContent = result.title;
                    const listItem = document.createElement('li');
                    listItem.appendChild(link);
                    searchResults.appendChild(listItem);
                });
            });
    });
}

// Add a click event listener to the mobile navbar button
const mobileNavbarButton = document.getElementById('mobileNavbarButton');
mobileNavbarButton.addEventListener('click', toggleMobileNav);

// Call the liveSearch function to enable live search
liveSearch();

$(document).ready(function () {
    // Define the URL to the search view
    var searchUrl = "{% url 'blog:search' %}";

    // Function to perform live search
    function performSearch() {
        var query = $("#search-input").val();
        if (query.length >= 3) {
            $.ajax({
                url: searchUrl,
                data: { q: query },
                dataType: 'json',
                success: function (data) {
                    displaySearchResults(data);
                }
            });
        } else {
            $("#search-results").html('').hide();
        }
    }

    // Function to display search results
    function displaySearchResults(results) {
        var resultList = $("#search-results");
        resultList.empty();

        if (results.length === 0) {
            resultList.append('<li>No results found</li>');
        } else {
            for (var i = 0; i < results.length; i++) {
                var result = results[i];
                resultList.append('<li><a href="' + result.url + '">' + result.title + '</a></li>');
            }
        }

        resultList.show();
    }

    // Handle search input changes
    $("#search-input").on('input', function () {
        performSearch();
    });

    // Handle form submission (optional)
    $("form").on('submit', function (e) {
        e.preventDefault();
        var query = $("#search-input").val();
        if (query.length >= 3) {
            window.location.href = searchUrl + '?q=' + query;
        }
    });
});
