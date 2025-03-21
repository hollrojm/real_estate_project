// API URLs
const API_PROPERTIES = '/api/properties/';
const API_OWNERS = '/api/owners/';
const API_PROPERTY_TYPES = '/api/property_types/';
const API_TRANSACTION_TYPES = '/api/transaction_types/';
const API_LOCATIONS = '/api/locations/';
const API_PROPERTY_AGES = '/api/properties/ages/';


// DOM Elements
const propertyTable = document.getElementById('propertyTable');
const propertyForm = document.getElementById('propertyForm');
const propertyModal = new bootstrap.Modal(document.getElementById('propertyModal'));

// Load all properties
function loadProperties() {
    fetch(API_PROPERTIES)
        .then(response => response.json())
        .then(data => {
            const tbody = propertyTable.querySelector('tbody');
            tbody.innerHTML = '';

            data.forEach(property => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${property.id}</td>
                    <td>${property.property_type_name || ''}</td>
                    <td>${property.owner_name || ''}</td>
                    <td>${property.address}</td>
                    <td>${property.department || ''}</td>
                    <td>${property.city || ''}</td>
                    <td>${property.district || ''}</td>
                    <td>${property.stratum || ''}</td>
                    <td>$${formatNumber(property.total_price)}</td>
                    <td>${property.area}</td>
                    <td>${property.floor || ''}</td>
                    <td>${property.age || ''}</td>
                    <td>${property.rooms || ''}</td>
                    <td>${property.latitude || ''}</td>
                    <td>${property.longitude || ''}</td>
                    <td>${property.publication_date || ''}</td>
                    <td>${property.publication_year || ''}</td>
                    <td>${property.publication_month || ''}</td>


                    <td>
                        <button class="btn btn-sm btn-primary edit-btn" data-id="${property.id}">Editar</button>
                        <button class="btn btn-sm btn-danger delete-btn" data-id="${property.id}">Eliminar</button>
                    </td>
                `;
                tbody.appendChild(row);
            });

            // Add event listeners to buttons
            document.querySelectorAll('.edit-btn').forEach(button => {
                button.addEventListener('click', () => editProperty(button.dataset.id));
            });

            document.querySelectorAll('.delete-btn').forEach(button => {
                button.addEventListener('click', () => deleteProperty(button.dataset.id));
            });
        })
        .catch(error => {
            console.error('Error loading properties:', error);
            showAlert('Error cargando propiedades', 'danger');
        });
}


function loadOwners() {
    fetch(API_OWNERS)
        .then(response => response.json())
        .then(data => {
            const ownerSelect = document.getElementById('owner');
            ownerSelect.innerHTML = '<option value="">Seleccionar...</option>';

            data.forEach(owner => {
                const option = document.createElement('option');
                option.value = owner.id;
                option.textContent = owner.name;
                ownerSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error loading owners:', error);
        });
}
function loadAges() {
    fetch(API_PROPERTY_AGES)
        .then(response => response.json())
        .then(data => {
            const ageSelect = document.getElementById('age');
            ageSelect.innerHTML = '<option value="">Seleccionar...</option>';
            data.forEach(age => {
                const option = document.createElement('option');
                option.value = age;
                option.textContent = age;
                ageSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error loading ages:', error);
        });
}
function loadPropertyType() {
    fetch(API_PROPERTY_TYPES)
        .then(response => response.json())
        .then(data => {
            const ownerSelect = document.getElementById('property_type');
            ownerSelect.innerHTML = '<option value="">Seleccionar...</option>';

            data.forEach(propertyType => {
                const option = document.createElement('option');
                option.value = propertyType.id;
                option.textContent = propertyType.name;
                ownerSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error loading Property Type:', error);
        });
}


function loadTransactionType() {
    fetch(API_TRANSACTION_TYPES)
        .then(response => response.json())
        .then(data => {
            const ownerSelect = document.getElementById('transaction_type');
            ownerSelect.innerHTML = '<option value="">Seleccionar...</option>';

            data.forEach(transactionType => {
                const option = document.createElement('option');
                option.value = transactionType.id;
                option.textContent = transactionType.name;
                ownerSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error loading Transaction type:', error);
        });
}
function loadDepartments() {
    fetch(API_LOCATIONS)
        .then(response => response.json())
        .then(data => {
            // Obtener departamentos únicos
            const departments = [...new Set(data.map(location => location.department))];

            const departmentSelect = document.getElementById('department');
            departmentSelect.innerHTML = '<option value="">Seleccionar...</option>';

            departments.forEach(department => {
                const option = document.createElement('option');
                option.value = department;
                option.textContent = department;
                departmentSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error loading departments:', error);
        });
}

// Manejar cambio de departamento
document.getElementById('department').addEventListener('change', function () {
    const department = this.value;
    if (!department) {
        // Restablecer selects dependientes
        document.getElementById('city').innerHTML = '<option value="">Seleccionar departamento primero...</option>';
        document.getElementById('district').innerHTML = '<option value="">Seleccionar ciudad primero...</option>';
        return;
    }

    // Cargar ciudades del departamento seleccionado
    fetch(`${API_LOCATIONS}by_department/?department=${encodeURIComponent(department)}`)
        .then(response => response.json())
        .then(data => {
            const citySelect = document.getElementById('city');
            citySelect.innerHTML = '<option value="">Seleccionar...</option>';

            // Añadir ciudades al select
            Object.keys(data).forEach(city => {
                const option = document.createElement('option');
                option.value = city;
                option.textContent = city;
                // Guardar los distritos como atributo de datos
                option.dataset.districts = JSON.stringify(data[city]);
                citySelect.appendChild(option);
            });

            // Restablecer select de distrito
            document.getElementById('district').innerHTML = '<option value="">Seleccionar ciudad primero...</option>';
        })
        .catch(error => {
            console.error('Error loading cities:', error);
        });
});

// Manejar cambio de ciudad
document.getElementById('city').addEventListener('change', function () {
    const selectedOption = this.options[this.selectedIndex];

    if (!selectedOption || !selectedOption.value) {
        document.getElementById('district').innerHTML = '<option value="">Seleccionar ciudad primero...</option>';
        return;
    }

    // Obtener distritos de la ciudad seleccionada
    try {
        const districts = JSON.parse(selectedOption.dataset.districts || '[]');

        const districtSelect = document.getElementById('district');
        districtSelect.innerHTML = '<option value="">Seleccionar...</option>';

        districts.forEach(district => {
            const option = document.createElement('option');
            option.value = district;
            option.textContent = district;
            districtSelect.appendChild(option);
        });
    } catch (e) {
        console.error('Error parsing districts data:', e);
    }
});


// Open modal for new property
document.getElementById('btnNewProperty').addEventListener('click', () => {
    document.getElementById('propertyId').value = '';
    propertyForm.reset();

    // Calculate price per m² automatically
    document.getElementById('total_price').addEventListener('input', calculatePricePerM2);
    document.getElementById('area').addEventListener('input', calculatePricePerM2);

    document.querySelector('.modal-title').textContent = 'Nueva Propiedad';
    propertyModal.show();
});


function calculatePricePerM2() {
    const price = parseFloat(document.getElementById('total_price').value) || 0;
    const area = parseFloat(document.getElementById('area').value) || 1;
    const pricePerM2 = price / area;
    // This will be calculated by the backend
}


document.getElementById('saveProperty').addEventListener('click', async () => {

    if (!propertyForm.checkValidity()) {
        propertyForm.reportValidity();
        return;
    }

    const propertyId = document.getElementById('propertyId').value;
    const isUpdate = propertyId !== '';
    try {

        const locationData = {
            department: document.getElementById('department').value,
            city: document.getElementById('city').value,
            district: document.getElementById('district').value
        };

        let locationId;
        const locationResponse = await fetch('/api/locations/find_or_create/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify(locationData)
        });

        if (locationResponse.ok) {
            const locationResult = await locationResponse.json();
            locationId = locationResult.id;
        } else {

            const createLocationResponse = await fetch('/api/locations/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify(locationData)
            });

            if (createLocationResponse.ok) {
                const newLocation = await createLocationResponse.json();
                locationId = newLocation.id;
            } else {
                throw new Error('No se pudo crear la ubicación');
            }
        }


        const property = {
            property_type: parseInt(document.getElementById('property_type').value),
            transaction_type: parseInt(document.getElementById('transaction_type').value),
            location: locationId,
            address: document.getElementById('address').value,
            area: parseFloat(document.getElementById('area').value),
            total_price: parseFloat(document.getElementById('total_price').value),
            price_by_m2: parseFloat((document.getElementById('total_price').value /
                document.getElementById('area').value).toFixed(2)),
            stratum: parseInt(document.getElementById('stratum').value || '0'),
            rooms: parseInt(document.getElementById('rooms').value || '0'),
            floor: parseInt(document.getElementById('floor').value || '0'),
            age: document.getElementById('age').value || null,
            onwer: parseInt(document.getElementById('owner').value),
            publication_date: new Date().toISOString().split('T')[0],
            publication_year: new Date().getFullYear(),
            publication_month: getMonthName(new Date().getMonth())
        };


        const url = isUpdate ? `${API_PROPERTIES}${propertyId}/` : API_PROPERTIES;
        const method = isUpdate ? 'PUT' : 'POST';

        const propertyResponse = await fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify(property)
        });

        if (!propertyResponse.ok) {
            const errorData = await propertyResponse.json();
            throw new Error(JSON.stringify(errorData));
        }

        showAlert(`Propiedad ${isUpdate ? 'actualizada' : 'creada'} exitosamente`, 'success');
        propertyModal.hide();
        loadProperties();

    } catch (error) {
        console.error('Error guardando propiedad:', error);
        try {
            const errorData = JSON.parse(error.message);
            showAlert(`Error: ${JSON.stringify(errorData)}`, 'danger');
        } catch (e) {
            showAlert(`Error: ${error.message}`, 'danger');
        }
    }
});


function editProperty(id) {
    fetch(`${API_PROPERTIES}${id}/`)
        .then(response => response.json())
        .then(async property => {
            document.getElementById('propertyId').value = property.id;
            document.getElementById('property_type').value = property.property_type;
            document.getElementById('transaction_type').value = property.transaction_type;


            let department = '';
            let city = '';
            let district = '';

            if (property.location) {

                const locationResponse = await fetch(`${API_LOCATIONS}${property.location}/`);
                if (locationResponse.ok) {
                    const location = await locationResponse.json();
                    department = location.department;
                    city = location.city;
                    district = location.district;
                }
            }

            // Establecer el departamento y esperar a que se cargue
            const departmentSelect = document.getElementById('department');
            departmentSelect.value = department;

            // Disparar el evento change para cargar las ciudades
            const changeEvent = new Event('change');
            departmentSelect.dispatchEvent(changeEvent);

            // Esperar a que se carguen las ciudades
            setTimeout(() => {
                const citySelect = document.getElementById('city');
                citySelect.value = city;

                // Disparar el evento change para cargar los distritos
                citySelect.dispatchEvent(changeEvent);

                // Esperar a que se carguen los distritos
                setTimeout(() => {
                    document.getElementById('district').value = district;
                }, 300);
            }, 300);

            document.getElementById('address').value = property.address;
            document.getElementById('area').value = property.area;
            document.getElementById('total_price').value = property.total_price;
            document.getElementById('stratum').value = property.stratum || '';
            document.getElementById('rooms').value = property.rooms || '';
            document.getElementById('floor').value = property.floor || '';
            document.getElementById('age').value = property.age || '';
            document.getElementById('owner').value = property.owner;

            document.querySelector('.modal-title').textContent = 'Editar Propiedad';
            propertyModal.show();
        })
        .catch(error => {
            console.error('Error loading property:', error);
            showAlert('Error cargando datos de la propiedad', 'danger');
        });
}
// Delete property
function deleteProperty(id) {
    if (confirm('¿Está seguro de eliminar esta propiedad?')) {
        fetch(`${API_PROPERTIES}${id}/`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
            .then(response => {
                if (response.ok) {
                    showAlert('Propiedad eliminada exitosamente', 'success');
                    loadProperties();
                } else {
                    throw new Error('Error al eliminar la propiedad');
                }
            })
            .catch(error => {
                console.error('Error deleting property:', error);
                showAlert('Error al eliminar la propiedad', 'danger');
            });
    }
}

// Helper function to show alerts
function showAlert(message, type) {
    const alertContainer = document.createElement('div');
    alertContainer.className = `alert alert-${type} alert-dismissible fade show`;
    alertContainer.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;

    const container = document.querySelector('.container');
    container.insertBefore(alertContainer, container.firstChild);

    // Auto hide after 5 seconds
    setTimeout(() => {
        alertContainer.classList.remove('show');
        setTimeout(() => alertContainer.remove(), 300);
    }, 5000);
}

// Helper function to format numbers
function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

// Helper function to get month name
function getMonthName(month) {
    const months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
    return months[month];
}

// Helper function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    loadProperties();
    loadOwners();
    loadPropertyType()
    loadTransactionType();
    loadDepartments();
    loadAges();
});