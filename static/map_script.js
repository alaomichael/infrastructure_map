var map;
var markers = [];
var data = [];

function initMap() {
    map = L.map('map').setView([7.3775, 3.9470], 7);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    fetch('static/school_data.json')
        .then(response => response.json())
        .then(jsonData => {
            data = jsonData;
            addMarkers(data);
        });

    fetch('static/filters.json')
        .then(response => response.json())
        .then(filters => {
            populateFilters(filters);
        });
}

// Function to add markers to the map
function addMarkers(data) {
    data.forEach(item => {
        var marker = L.marker([item.LATITUDE, item.LONGITUDE]).addTo(map)
            .bindPopup(`
                <b>Name of School:</b> ${item['NAME OF SCHOOL']}<br>
                <b>Category:</b> ${item.CATEGORY}<br>
                <b>State:</b> ${item.STATE}<br>
                <b>Local Govt Area:</b> ${item.LGAs}<br>
                <b>Ward:</b> ${item.WARD}<br>
                <b>Level of Dilapidation:</b> ${item['LEVEL OF DILAPIDATION']}<br>
                <b>Infrastructure Need:</b><ul>
                    ${item['INFRASTRUCTURAL NEEDS'].split(',').map(need => `<li>${need.trim()}</li>`).join('')}
                </ul><br>
                <img src="${item.IMAGE}" width="100%" height="auto">
            `);
        markers.push({
            marker: marker,
            state: item.STATE,
            category: item.CATEGORY,
            lga: item.LGAs,
            ward: item.WARD,
            level_of_dilapidation: item['LEVEL OF DILAPIDATION'],
            infrastructure_need: item['INFRASTRUCTURAL NEEDS']
        });
    });
}

// Function to populate filter options
function populateFilters(filters) {
    populateDropdown('filter-state', filters.states);
    populateDropdown('filter-category', filters.category);
    populateDropdown('filter-lga', filters.lgas);
    populateDropdown('filter-ward', filters.wards);
    populateDropdown('filter-level_of_dilapidation', filters.levels_of_dilapidation);
    populateDropdown('filter-infrastructure_need', filters.infrastructure_needs);
}

function populateDropdown(id, options) {
    var select = document.getElementById(id);
    options.forEach(option => {
        var opt = document.createElement('option');
        opt.value = option;
        opt.innerHTML = option;
        select.appendChild(opt);
    });
}

function filterMap() {
    var filterState = document.getElementById('filter-state').value;
    var filterCategory = document.getElementById('filter-category').value;
    var filterLGA = document.getElementById('filter-lga').value;
    var filterWard = document.getElementById('filter-ward').value;
    var filterLevelOfDilapidation = document.getElementById('filter-level_of_dilapidation').value;
    var filterInfrastructureNeed = document.getElementById('filter-infrastructure_need').value;

    markers.forEach(item => {
        map.removeLayer(item.marker);
    });

    markers.forEach(item => {
        if ((filterState === 'all' || item.state === filterState) &&
            (filterCategory === 'all' || item.category === filterCategory) &&
            (filterLGA === 'all' || item.lga === filterLGA) &&
            (filterWard === 'all' || item.ward === filterWard) &&
            (filterLevelOfDilapidation === 'all' || item.level_of_dilapidation === filterLevelOfDilapidation) &&
            (filterInfrastructureNeed === 'all' || item.infrastructure_need.includes(filterInfrastructureNeed))) {
            item.marker.addTo(map);
        }
    });
}

document.addEventListener('DOMContentLoaded', initMap);
