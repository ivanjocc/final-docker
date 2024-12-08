import Navbar from "../components/Navbar";
import Link from "next/link";
import styles from "../styles/Home.module.css";

export default function Offers() {
  const jobOffers = [
    { id: 1, title: "Desarrollador Backend", company: "Empresa A" },
    { id: 2, title: "Desarrollador Frontend", company: "Empresa B" },
    { id: 3, title: "Data Scientist", company: "Empresa C" },
  ];

  return (
    <div className={styles.container}>
      <Navbar />
      <h1>Ofertas de Trabajo</h1>
      <ul>
        {jobOffers.map((offer) => (
          <li key={offer.id}>
            <Link href={`/offers/${offer.id}`}>
              {offer.title} - {offer.company}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
