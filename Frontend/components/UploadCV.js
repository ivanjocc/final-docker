import { useState } from "react";

export default function UploadCV() {
  const [file, setFile] = useState(null);
  const [skills, setSkills] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

    setLoading(true);
    setError("");

    const reader = new FileReader();
    reader.onload = async () => {
      const text = reader.result;

      try {
        const response = await fetch("http://localhost:8001/extract_skills", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            name: file.name,
            text: text,
          }),
        });

        if (!response.ok) {
          throw new Error("Error en el servidor al procesar el CV.");
        }

        const data = await response.json();
        setSkills(data.skills);
        setLoading(false);
      } catch (error) {
        setError(error.message);
        setLoading(false);
      }
    };

    reader.readAsText(file);
  };

  return (
    <div>
      <h2>Sube tu CV</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit" disabled={loading}>
          {loading ? "Cargando..." : "Subir CV"}
        </button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}
      {skills && (
        <div>
          <h3>Habilidades Extraídas</h3>
          <ul>
            {skills.map((skill, index) => (
              <li key={index}>{skill}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
