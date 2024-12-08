import Navbar from "../components/Navbar";
import Link from "next/link";
import styles from "../styles/Home.module.css";

export default function Home() {
  return (
    <div className={styles.container}>
      <Navbar />
      <h1>Bienvenido a la Plataforma de Reclutamiento</h1>
      <Link href="/offers">Ver Ofertas de Trabajo</Link>
    </div>
  );
}
