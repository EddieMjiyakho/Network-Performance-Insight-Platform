// api/dataApi.js
export const fetchDataFromAPI = async (filters) => {
  try {
    // Convert filters object to URL query parameters
    const params = new URLSearchParams(filters);
    const url = `api/isp-data/?${params.toString()}`;

    const response = await fetch(url);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};