document.addEventListener('DOMContentLoaded', () => {
    const containers = document.querySelectorAll('.box');
    let activeContainer = null;
    let offsetX, offsetY;

    containers.forEach(container => {
        container.addEventListener('mousedown', (e) => {
            activeContainer = container;
            offsetX = e.clientX - container.getBoundingClientRect().left;
            offsetY = e.clientY - container.getBoundingClientRect().top;

            container.style.zIndex = 1;
        });
    });

    document.addEventListener('mousemove', (e) => {
        if (activeContainer) {
            activeContainer.style.left = (e.clientX - offsetX) + 'px';
            activeContainer.style.top = (e.clientY - offsetY) + 'px';
        }
    });

    document.addEventListener('mouseup', () => {
        if (activeContainer) {
            activeContainer.style.zIndex = 0;
            activeContainer = null;
        }
    });
});
