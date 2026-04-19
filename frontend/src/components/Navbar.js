"use client";
import Link from 'next/link';
import { Bell, ShoppingBag, User, History } from 'lucide-react';
import styles from './Navbar.module.css';

export default function Navbar({ variant = "home" }) {
  return (
    <nav className={styles.navbar}>
      <div className={styles.logoContainer}>
        <Link href="/" className={styles.logo}>
          <span className="text-red font-bold">Zomato</span>
          <span className="text-red font-medium"> AI</span>
        </Link>
      </div>

      {variant === "home" && (
        <div className={styles.navLinks}>
          <Link href="/" className={`${styles.link} ${styles.active}`}>AI Concierge</Link>
          <Link href="/discovery" className={styles.link}>Discovery</Link>
          <Link href="/orders" className={styles.link}>Orders</Link>
        </div>
      )}

      <div className={styles.actions}>
        <button className={styles.iconBtn}><Bell size={20} /></button>
        {variant === "home" ? (
          <button className={styles.iconBtn}><ShoppingBag size={20} /></button>
        ) : (
          <button className={styles.iconBtn}><History size={20} /></button>
        )}
        <div className={styles.avatar}>
          <User size={18} color="#fff" />
        </div>
      </div>
    </nav>
  );
}
