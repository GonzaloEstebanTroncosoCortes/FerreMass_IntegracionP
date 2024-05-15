import React, { useState, useEffect } from 'react';

function Test() {
  const [productos, setProductos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8000/erp/productos_disponibles_bodega/')
      .then(response => {
        if (!response.ok) {
          throw new Error('Error al obtener los datos');
        }
        return response.json();
      })
      .then(data => {
        setLoading(false);
        if (data.length === 0) {
          setError('No hay productos disponibles en la bodega');
        } else {
          setProductos(data);
        }
      })
      .catch(error => {
        setLoading(false);
        setError('Error de conexión: ' + error.message);
      });
  }, []);

  if (loading) {
    return <div>Cargando...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h1>Productos Disponibles en Bodega</h1>
      {productos.length > 0 ? (
        <table>
          <thead>
            <tr>
              <th>Código del Producto</th>
              <th>Marca</th>
              <th>Código</th>
              <th>Nombre</th>
              <th>Categoría</th>
              <th>Stock</th>
            </tr>
          </thead>
          <tbody>
            {productos.map(producto => (
              <tr key={producto.codigo_producto}>
                <td>{producto.codigo_producto}</td>
                <td>{producto.marca}</td>
                <td>{producto.codigo}</td>
                <td>{producto.nombre}</td>
                <td>{producto.categoria}</td>
                <td>{producto.stock}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <div>No hay productos disponibles en la bodega</div>
      )}
    </div>
  );
}

export default Test;

