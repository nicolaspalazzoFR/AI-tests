// Gear Characteristics Interactive Mockup
// Dynamically renders forms based on gear type selection

// Initialize app on load
document.addEventListener('DOMContentLoaded', initializeApp);

let currentHighlightIndex = -1;
let searchResults = [];

function initializeApp() {
    setupEventListeners();
}

// Setup event listeners
function setupEventListeners() {
    const searchInput = document.getElementById('gearSearch');
    searchInput.addEventListener('input', handleSearchInput);
    searchInput.addEventListener('focus', handleSearchFocus);
    searchInput.addEventListener('keydown', handleKeyboardNavigation);
    
    // Close results when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.search-wrapper')) {
            hideSearchResults();
        }
    });
}

// Handle search input
function handleSearchInput(event) {
    const query = event.target.value.trim().toLowerCase();
    
    if (query.length === 0) {
        hideSearchResults();
        return;
    }
    
    // Search gear types by code or name
    searchResults = Object.keys(GEAR_DATA)
        .filter(code => {
            const gear = GEAR_DATA[code];
            return code.toLowerCase().includes(query) || 
                   gear.name.toLowerCase().includes(query);
        })
        .sort();
    
    displaySearchResults(searchResults, query);
}

// Handle search focus
function handleSearchFocus(event) {
    if (event.target.value.trim().length > 0) {
        handleSearchInput(event);
    }
}

// Handle keyboard navigation
function handleKeyboardNavigation(event) {
    const resultsDiv = document.getElementById('searchResults');
    if (resultsDiv.style.display === 'none') return;
    
    const items = resultsDiv.querySelectorAll('.search-result-item');
    
    if (event.key === 'ArrowDown') {
        event.preventDefault();
        currentHighlightIndex = Math.min(currentHighlightIndex + 1, items.length - 1);
        updateHighlight(items);
    } else if (event.key === 'ArrowUp') {
        event.preventDefault();
        currentHighlightIndex = Math.max(currentHighlightIndex - 1, -1);
        updateHighlight(items);
    } else if (event.key === 'Enter') {
        event.preventDefault();
        if (currentHighlightIndex >= 0 && currentHighlightIndex < searchResults.length) {
            selectGear(searchResults[currentHighlightIndex]);
        }
    } else if (event.key === 'Escape') {
        hideSearchResults();
    }
}

// Update highlight
function updateHighlight(items) {
    items.forEach((item, index) => {
        if (index === currentHighlightIndex) {
            item.classList.add('highlighted');
            item.scrollIntoView({ block: 'nearest' });
        } else {
            item.classList.remove('highlighted');
        }
    });
}

// Display search results
function displaySearchResults(results, query) {
    const resultsDiv = document.getElementById('searchResults');
    resultsDiv.innerHTML = '';
    currentHighlightIndex = -1;
    
    if (results.length === 0) {
        resultsDiv.innerHTML = '<div class="no-results">No matching gear types found</div>';
        resultsDiv.style.display = 'block';
        return;
    }
    
    // Add result count
    const countDiv = document.createElement('div');
    countDiv.className = 'result-count';
    countDiv.textContent = `${results.length} gear type${results.length > 1 ? 's' : ''} found`;
    resultsDiv.appendChild(countDiv);
    
    // Add results
    results.forEach(code => {
        const gear = GEAR_DATA[code];
        const item = document.createElement('div');
        item.className = 'search-result-item';
        item.innerHTML = `
            <span class="result-code">${code}</span>
            <span class="result-name">${gear.name}</span>
        `;
        item.addEventListener('click', () => selectGear(code));
        resultsDiv.appendChild(item);
    });
    
    resultsDiv.style.display = 'block';
}

// Hide search results
function hideSearchResults() {
    document.getElementById('searchResults').style.display = 'none';
    currentHighlightIndex = -1;
}

// Select a gear
function selectGear(gearCode) {
    const searchInput = document.getElementById('gearSearch');
    const gear = GEAR_DATA[gearCode];
    
    searchInput.value = `${gearCode} - ${gear.name}`;
    hideSearchResults();
    renderGearForm(gear);
}

// Show empty state
function showEmptyState() {
    document.getElementById('formContainer').style.display = 'none';
    document.getElementById('emptyState').style.display = 'flex';
}

// Render gear form
function renderGearForm(gear) {
    // Hide empty state, show form
    document.getElementById('emptyState').style.display = 'none';
    document.getElementById('formContainer').style.display = 'block';
    
    // Set gear title and code
    document.getElementById('gearTitle').textContent = gear.name;
    document.getElementById('gearCode').textContent = gear.code;
    
    // Render mandatory fields
    const mandatoryContainer = document.getElementById('mandatoryFields');
    mandatoryContainer.innerHTML = '';
    gear.mandatory.forEach(field => {
        mandatoryContainer.appendChild(createFieldElement(field, true));
    });
    
    // Render optional fields
    const optionalContainer = document.getElementById('optionalFields');
    const optionalSection = document.getElementById('optionalSection');
    
    if (gear.optional.length > 0) {
        optionalSection.style.display = 'block';
        optionalContainer.innerHTML = '';
        gear.optional.forEach(field => {
            optionalContainer.appendChild(createFieldElement(field, false));
        });
    } else {
        optionalSection.style.display = 'none';
    }
    
    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Create field element based on type
function createFieldElement(field, isMandatory) {
    const fieldGroup = document.createElement('div');
    fieldGroup.className = 'field-group';
    
    // Label
    const label = document.createElement('label');
    label.className = 'field-label';
    label.innerHTML = `
        ${field.description}
        <span class="field-code">(${field.code})</span>
        ${isMandatory ? '<span class="required-asterisk">*</span>' : ''}
        ${field.code === 'HS' ? '<span class="new-badge">New 2026</span>' : ''}
    `;
    fieldGroup.appendChild(label);
    
    // Input element based on type
    if (field.type === 'CODE') {
        fieldGroup.appendChild(createCodeInput(field));
    } else if (field.type === 'TEXT' && field.code === 'GD') {
        fieldGroup.appendChild(createTextArea(field));
    } else if (field.type === 'TEXT') {
        fieldGroup.appendChild(createTextInput(field));
    } else {
        fieldGroup.appendChild(createNumericInput(field));
    }
    
    return fieldGroup;
}

// Create CODE type input (dropdown)
function createCodeInput(field) {
    const select = document.createElement('select');
    select.className = 'field-input';
    select.id = `field_${field.code}`;
    
    // Default option
    let placeholder = 'Select...';
    if (field.code === 'MS') placeholder = 'Select mesh type';
    if (field.code === 'DA') placeholder = 'Select attachments...';
    if (field.code === 'TT') placeholder = 'Select twine type';
    
    const defaultOption = document.createElement('option');
    defaultOption.value = '';
    defaultOption.textContent = placeholder;
    select.appendChild(defaultOption);
    
    // Add options based on field code
    let options = [];
    if (field.code === 'MS') {
        options = MESH_TYPES;
    } else if (field.code === 'DA') {
        options = DEVICES_ATTACHMENTS;
    } else if (field.code === 'TT') {
        options = ['Mono', 'Multi', 'Braided'];
    }
    
    options.forEach(opt => {
        const option = document.createElement('option');
        option.value = opt;
        option.textContent = opt;
        select.appendChild(option);
    });
    
    return select;
}

// Create text area
function createTextArea(field) {
    const textarea = document.createElement('textarea');
    textarea.className = 'field-input';
    textarea.id = `field_${field.code}`;
    textarea.placeholder = 'Enter description...';
    return textarea;
}

// Create text input
function createTextInput(field) {
    const input = document.createElement('input');
    input.type = 'text';
    input.className = 'field-input';
    input.id = `field_${field.code}`;
    input.placeholder = 'Enter value...';
    return input;
}

// Create numeric input with unit
function createNumericInput(field) {
    const wrapper = document.createElement('div');
    wrapper.className = 'input-wrapper';
    
    const input = document.createElement('input');
    input.type = 'number';
    input.step = field.unit === 'MTR' || field.unit === 'MMT' ? '0.01' : '1';
    input.className = 'field-input';
    input.id = `field_${field.code}`;
    input.placeholder = '0';
    wrapper.appendChild(input);
    
    // Add unit label
    if (field.unit) {
        const unitLabel = document.createElement('span');
        unitLabel.className = 'unit-label';
        
        let unitText = field.unit;
        if (field.unit === 'MTR') unitText = 'm';
        if (field.unit === 'MMT') unitText = 'mm';
        if (field.unit === 'C62') unitText = 'pieces';
        if (field.unit === 'hooks') unitText = 'hooks';
        if (field.unit === 'lines') unitText = 'lines';
        
        unitLabel.textContent = unitText;
        wrapper.appendChild(unitLabel);
    }
    
    return wrapper;
}

// Reset form
function resetForm() {
    document.getElementById('gearSearch').value = '';
    hideSearchResults();
    showEmptyState();
}

// Save gear (mock function)
function saveGear() {
    const searchValue = document.getElementById('gearSearch').value;
    const gearCode = document.getElementById('gearCode').textContent;
    if (!gearCode) return;
    
    // Collect form data
    const gearData = GEAR_DATA[gearCode];
    const formData = {
        gearType: gearCode,
        gearName: gearData.name,
        fields: {}
    };
    
    // Get all field values
    [...gearData.mandatory, ...gearData.optional].forEach(field => {
        const input = document.getElementById(`field_${field.code}`);
        if (input && input.value) {
            formData.fields[field.code] = input.value;
        }
    });
    
    // Show success message
    alert(`Gear saved! (Mock)\n\nGear: ${formData.gearName}\nFields captured: ${Object.keys(formData.fields).length}`);
    console.log('Saved gear data:', formData);
}

// Helper function to get unit display text
function getUnitDisplay(unit) {
    const unitMap = {
        'MTR': 'm',
        'MMT': 'mm',
        'C62': 'pieces'
    };
    return unitMap[unit] || unit || '';
}
