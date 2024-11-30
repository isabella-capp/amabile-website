const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

/**
 * Adds an event listener to the 'signUpButton' element.
 * Activates the right panel by adding the 'right-panel-active' class to the container.
 * @event click
 */
signUpButton.addEventListener('click', () => {
    container.classList.add('right-panel-active');
});

/**
 * Adds an event listener to the 'signInButton' element.
 * Deactivates the right panel by removing the 'right-panel-active' class from the container.
 * @event click
 */
signInButton.addEventListener('click', () => {
    container.classList.remove('right-panel-active');
});

/**
 * Handles form submission by sending user input data to the server via a POST request.
 * Prevents default form submission behavior and logs the input values for debugging.
 * Sends the data in JSON format to the '/api/contact' endpoint.
 * Displays a success message if the request is successful or an error message otherwise.
 * @async
 * @param {Event} event - The submit event triggered by the form submission.
 */

async function submitFormContact(event) {
        event.preventDefault();

        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const phone = document.getElementById('phonenumber').value;
        const description = document.getElementById('description').value;

        console.log(name);
        console.log(email);
        console.log(phone);
        console.log(description);

        const response = await fetch('/api/contact', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({name, email, phone, description})
        });

        const result = await response.json()
        if(response.ok){
            alert("Contact added successfully");

            document.getElementById('name').value = "";
            document.getElementById('email').value = "";
            document.getElementById('phonenumber').value = "";
            document.getElementById('description').value = "";
        }else {
            alert(`Error: ${result.error}`);
        }
    }

    async function submitFormNewsletter(event) {
        event.preventDefault();
        const email = document.getElementById('email').value;

        const response = await fetch('/api/newsletter', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({email})
        });

        const result = await response.json()
        if(response.ok){
            alert("Email contact added successfully");
            document.getElementById('email').value = "";
        }else {
            alert(`Error: ${result.error}`);
        }
    }