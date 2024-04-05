function fetchApi() {
    let container = document.getElementById("fetch-results");

    const url = "https://reqres.in/api/users";

    fetch(url, {
        method: "GET",
        headers: {
            "X-Request-with": "",
            "X-CSRFToken": "{{ csrf_token }}"
        }
    })
    .then((response) => response.json())
    .then((response) => {
        let cards = ``;

        for (const person of response.data) {
            let card = `
            <div class="card" style="width: 18rem;">
                <div class="card-body">
                <h5 class="card-title">${person.first_name} ${person.last_name}</h5>
                <p class="card-text">Email: ${person.email}</p>
                </div>
            </div>
            `
            cards += card;
        }
        container.innerHTML = cards;
    })
    .catch((error) => console.log(error))

}