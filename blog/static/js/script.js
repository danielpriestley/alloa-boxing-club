const hamburger = document.getElementById('openSidebarMenu');

hamburger.addEventListener('click', function () {
    const navigation = document.getElementById('left-nav');

    navigation.classList.toggle("hidden");
});