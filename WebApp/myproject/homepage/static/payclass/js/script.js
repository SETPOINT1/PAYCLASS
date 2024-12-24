const dots = document.querySelectorAll('.dot');
const images = document.querySelectorAll('.slide img');

dots.forEach((dot) => {
  dot.addEventListener('click', () => {
    // ลบคลาส active จากรูปภาพและปุ่มทั้งหมด
    images.forEach((img) => img.classList.remove('active'));
    dots.forEach((d) => d.classList.remove('active'));

    // เพิ่มคลาส active ให้กับรูปและปุ่มที่คลิก
    const index = dot.dataset.index;
    images[index].classList.add('active');
    dot.classList.add('active');
  });
});
