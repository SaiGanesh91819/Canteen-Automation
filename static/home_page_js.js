document.addEventListener('DOMContentLoaded', () => {
    const toggleThemeButton = document.getElementById('toggle_theme');
    const themeIcon = document.getElementById('theme_icon');
    const currentTheme = localStorage.getItem('theme') || 'light';
    setTheme(currentTheme);

    toggleThemeButton.addEventListener('click', () => {
        const theme = document.body.classList.contains('dark-theme') ? 'light' : 'dark';
        setTheme(theme);
    });

    function setTheme(theme) {
        document.body.classList.toggle('dark-theme', theme === 'dark');
        themeIcon.src = theme === 'dark' ? themeIcon.dataset.dark : themeIcon.dataset.light;
        localStorage.setItem('theme', theme);
    }

    const profileTrigger = document.getElementById("profile-trigger");
    const dropdownMenu = document.getElementById("dropdown-menu");   
    profileTrigger.addEventListener("click", () => {
        dropdownMenu.style.display = "block";
    });    
    profileTrigger.addEventListener("mouseleave", () => {
        setTimeout(() => {
            if (!dropdownMenu.matches(":hover")) {
                dropdownMenu.style.display = "none";
            }
        }, 200);
    });
    dropdownMenu.addEventListener("mouseleave", () => {
        dropdownMenu.style.display = "none";
    });
});
