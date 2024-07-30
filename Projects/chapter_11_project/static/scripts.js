document.addEventListener('DOMContentLoaded', function() {
    const booksTable = document.getElementById('books-table').querySelector('tbody');
    const addBookForm = document.getElementById('add-book-form');

    addBookForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const title = this.title.value;
        const author = this.author.value;
        const category = this.category.value;
        const status = this.status.value;

        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${title}</td>
            <td>${author}</td>
            <td>${category}</td>
            <td><button class="toggle-status" data-status="${status}">${capitalizeFirstLetter(status)}</button></td>
            <td>
                <button class="edit-book">Edit</button>
                <button class="delete-book">Delete</button>
            </td>
        `;

        booksTable.appendChild(row);
        this.reset();
    });

    booksTable.addEventListener('click', function(e) {
        if (e.target.classList.contains('delete-book')) {
            const row = e.target.closest('tr');
            row.remove();
        }

        if (e.target.classList.contains('toggle-status')) {
            const button = e.target;
            const currentStatus = button.getAttribute('data-status');
            const newStatus = currentStatus === 'available' ? 'borrowed' : '
