import { useState } from "react";

export default function Home() {
  const [mesh, setMesh] = useState(null);
  const [image, setImage] = useState(null);

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    setImage(URL.createObjectURL(file));
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://127.0.0.1:8000/upload/", {
      method: "POST",
      body: formData,
    });
    const data = await res.json();
    setMesh(data.mesh);
  };

  return (
    <div>
      <h1>AI 3D Product Viewer</h1>
      <input type="file" onChange={handleUpload} />
      {image && <img src={image} width={200} />}
      {mesh && (
        <iframe
          src={`/uploads/${mesh}`}
          width="600"
          height="400"
          title="3D Mesh Viewer"
        ></iframe>
      )}
    </div>
  );
}
