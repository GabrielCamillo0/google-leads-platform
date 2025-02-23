export async function fetchLeads() {
    const response = await fetch("http://127.0.0.1:8000/leads");
    return await response.json();
}
