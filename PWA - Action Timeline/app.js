// Search functionality
const searchInput = document.getElementById('searchInput');
const clearBtn = document.getElementById('clearBtn');
const actionCards = document.querySelectorAll('.action-card');
const groupedViewBtn = document.getElementById('groupedViewBtn');
const chronoViewBtn = document.getElementById('chronoViewBtn');
const timeline = document.querySelector('.timeline');
const categoriesContainer = document.getElementById('categoriesContainer');
const chronoContainer = document.getElementById('chronoContainer');
const categoryHeaders = document.querySelectorAll('.category-header');

// Initialize chronological view
function initChronologicalView() {
    // Clone all action cards to chronological container
    actionCards.forEach(card => {
        const clone = card.cloneNode(true);
        chronoContainer.appendChild(clone);
    });
}

// Search functionality
searchInput.addEventListener('input', (e) => {
    const searchTerm = e.target.value.toLowerCase();
    let visibleCount = 0;
    
    actionCards.forEach(card => {
        const date = card.getAttribute('data-date').toLowerCase();
        const keywords = card.getAttribute('data-keywords').toLowerCase();
        const action = card.querySelector('.action').textContent.toLowerCase();
        const tool = card.querySelector('.tool').textContent.toLowerCase();
        
        if (date.includes(searchTerm) || 
            keywords.includes(searchTerm) || 
            action.includes(searchTerm) ||
            tool.includes(searchTerm)) {
            card.style.display = '';
            visibleCount++;
        } else {
            card.style.display = 'none';
        }
    });
    
    // Update category visibility and counts
    document.querySelectorAll('.category-section').forEach(section => {
        const visibleCards = section.querySelectorAll('.action-card:not([style*="display: none"])');
        if (visibleCards.length === 0) {
            section.style.display = 'none';
        } else {
            section.style.display = '';
        }
    });
    
    clearBtn.style.display = searchTerm ? 'block' : 'none';
});

clearBtn.addEventListener('click', () => {
    searchInput.value = '';
    searchInput.dispatchEvent(new Event('input'));
    searchInput.focus();
});

// View toggle functionality
groupedViewBtn.addEventListener('click', () => {
    timeline.classList.add('grouped-view');
    timeline.classList.remove('chrono-view');
    categoriesContainer.style.display = '';
    chronoContainer.style.display = 'none';
    groupedViewBtn.classList.add('active');
    chronoViewBtn.classList.remove('active');
});

chronoViewBtn.addEventListener('click', () => {
    timeline.classList.remove('grouped-view');
    timeline.classList.add('chrono-view');
    categoriesContainer.style.display = 'none';
    chronoContainer.style.display = '';
    groupedViewBtn.classList.remove('active');
    chronoViewBtn.classList.add('active');
});

// Category collapse functionality
function toggleCategory(header) {
    const section = header.closest('.category-section');
    section.classList.toggle('collapsed');
}

// Initialize the page
document.addEventListener('DOMContentLoaded', () => {
    initChronologicalView();
    clearBtn.style.display = 'none';
});

// Keyboard shortcuts
document.addEventListener('keydown', (e) => {
    // Ctrl/Cmd + K to focus search
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        searchInput.focus();
        searchInput.select();
    }
    
    // Escape to clear search
    if (e.key === 'Escape' && document.activeElement === searchInput) {
        searchInput.value = '';
        searchInput.dispatchEvent(new Event('input'));
    }
});
