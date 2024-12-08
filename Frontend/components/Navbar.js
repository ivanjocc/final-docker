import { useState } from "react";

export default function UploadCV() {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

    // Aquí puedes agregar lógica para subir el CV
    console.log("CV uploaded:", file);
  };

  return (
    <div>
      <h2>Sube tu CV</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Subir CV</button>
      </form>
    </div>
  );
}
