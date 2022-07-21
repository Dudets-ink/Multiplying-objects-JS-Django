function addForm(){
    const button = document.getElementById('buttonAddForm');

    button.addEventListener("click", function(){
        const inputClass = document.getElementById('input-form');
        const inputForm = document.getElementById('empty-input').cloneNode(true);
        const currentFormCount = document.getElementsByClassName('input-class').length;
        const totalFormsets = document.getElementById('total-formsets');
        const regex = new RegExp('__prefix__', 'g')
        inputForm.innerHTML = inputForm.innerHTML.replace(regex, currentFormCount-1)

        inputForm.setAttribute('class', 'input-class');
        inputForm.setAttribute('id', `form-${currentFormCount}`);
        inputClass.append(inputForm);
        totalFormsets.setAttribute('value', currentFormCount)
    });
};