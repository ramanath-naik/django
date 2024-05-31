// document.addEventListener('DOMContentLoaded', () => {
//     loadDepartments();
//     loadEmployees();

//     document.getElementById('department-form').addEventListener('submit', saveDepartment);
//     document.getElementById('employee-form').addEventListener('submit', saveEmployee);
//     document.getElementById('file-upload-form').addEventListener('submit', uploadFile);
// });

// async function loadDepartments() {
//     const response = await fetch('/api/departments/');
//     const departments = await response.json();
//     const departmentList = document.getElementById('department-list');
//     departmentList.innerHTML = '';
//     departments.forEach(department => {
//         const li = document.createElement('li');
//         li.textContent = department.DepartmentName;
//         departmentList.appendChild(li);
//     });
// }

// async function loadEmployees() {
//     const response = await fetch('/api/employees/');
//     const employees = await response.json();
//     const employeeList = document.getElementById('employee-list');
//     employeeList.innerHTML = '';
//     employees.forEach(employee => {
//         const li = document.createElement('li');
//         li.textContent = `${employee.EmployeeName} (${employee.Department})`;
//         employeeList.appendChild(li);
//     });
// }

// async function saveDepartment(event) {
//     event.preventDefault();
//     const departmentName = document.getElementById('department-name').value;
//     const id = document.getElementById('department-id').value;
//     const url = id ? `/api/departments/${id}/` : '/api/departments/';
//     const method = id ? 'PUT' : 'POST';
//     const response = await fetch(url, {
//         method: method,
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({ DepartmentName: departmentName })
//     });
//     const result = await response.json();
//     alert(result);
//     loadDepartments();
//     document.getElementById('department-form').reset();
// }

// async function saveEmployee(event) {
//     event.preventDefault();
//     const employeeName = document.getElementById('employee-name').value;
//     const employeeDepartment = document.getElementById('employee-department').value;
//     const id = document.getElementById('employee-id').value;
//     const url = id ? `/api/employees/${id}/` : '/api/employees/';
//     const method = id ? 'PUT' : 'POST';
//     const response = await fetch(url, {
//         method: method,
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({ EmployeeName: employeeName, Department: employeeDepartment })
//     });
//     const result = await response.json();
//     alert(result);
//     loadEmployees();
//     document.getElementById('employee-form').reset();
// }

// async function uploadFile(event) {
//     event.preventDefault();
//     const fileInput = document.getElementById('file-input');
//     const formData = new FormData();
//     formData.append('file', fileInput.files[0]);
//     const response = await fetch('/api/savefile/', {
//         method: 'POST',
//         body: formData
//     });
//     const result = await response.json();
//     document.getElementById('file-upload-status').textContent = result;
// }


// to add csrf token in the header

// document.getElementById('department-form').addEventListener('submit', function(event) {
//     event.preventDefault(); // Prevent the default form submission

//     // Get the department name from the input field
//     var departmentName = document.getElementById('department-name').value;

//     // Prepare the department data to be sent in the POST request
//     var departmentData = {
//         "DepartmentName": departmentName
//     };

//     // Make an HTTP POST request to the Django API endpoint
//     fetch('/api/departments/', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': getCookie('csrftoken') // Add CSRF token for security
//         },
//         body: JSON.stringify(departmentData)
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log(data); 
//         // Optionally, reset the form and show a success message
//         document.getElementById('department-form').reset();
//         alert('Department added successfully');
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// });

// // Function to get CSRF token from cookies
// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }




document.getElementById('department-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    var departmentName = document.getElementById('department-name').value;

    var departmentData = {
        "DepartmentName": departmentName
    };

    fetch('/api/departments/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(departmentData)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Reset the form after a successful submission
        document.getElementById('department-form').reset();
        alert('Department added successfully');
    })
    .catch(error => {
        console.error('Error:', error);
    });

});


async function viewAllDepartments() {
    try {
        const response = await fetch('/api/departments/');
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        const departments = await response.json();
        console.log("data",departments)

        const tableBody = document.getElementById('department-table-body');
        tableBody.innerHTML = ''; // Clear previous table data

        departments.forEach(function(department) {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${department.DepartmentId}</td>
                <td>${department.DepartmentName}</td>
            `;
            tableBody.appendChild(row);
        });
    } catch (error) {
        console.error('Error:', error);
    }
}

document.getElementById('view-all-departments').addEventListener('click', viewAllDepartments);
