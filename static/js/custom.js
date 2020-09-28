const showClientTable = () => {
    const clientDetailTable = document.getElementById('client_details');
    const display = clientDetailTable.style.display;
    clientDetailTable.style.display = display === "none" ? "table" : "none"
};