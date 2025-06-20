function toggleForm() {
    const loginForm = document.getElementById('loginForm');
    const signupForm = document.getElementById('signupForm');
    const mode = document.getElementsByClassName('mode')[0];
    
    loginForm.classList.toggle('hidden');
    signupForm.classList.toggle('hidden');
        
     
}
