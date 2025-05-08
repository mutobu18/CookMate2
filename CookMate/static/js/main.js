// recipes.js

const buttons = document.querySelectorAll('.see-recipe');

buttons.forEach(button => {
  button.addEventListener('click', () => {
    const recipeUrl = button.getAttribute('data-url');
    window.location.href = recipeUrl;
  });
});