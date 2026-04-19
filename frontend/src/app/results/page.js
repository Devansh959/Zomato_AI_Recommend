"use client";
import Link from 'next/link';
import { Sparkles, MapPin, SlidersHorizontal, ArrowLeft, Star } from 'lucide-react';
import Navbar from '../../components/Navbar';
import styles from './page.module.css';

export default function Results() {
  const mockResults = [
    {
      id: 1,
      name: "Golden Dragon",
      location: "Colaba, Mumbai",
      budget: "$$",
      rating: "4.8",
      reviews: "1.2k",
      image: "file:///C:/Users/devan/.gemini/antigravity/brain/9f3a143b-df66-4d07-9a71-81d1cda2e72b/golden_dragon_food_1776545832984.png",
      aiHighlight: "Iconic for its fiery Schezwan Fried Rice. High match for authentic taste.",
      actionText: "Book Table"
    },
    {
      id: 2,
      name: "Chilli & Spice",
      location: "Bandra West, Mumbai",
      budget: "$$",
      rating: "4.5",
      reviews: "850",
      image: "file:///C:/Users/devan/.gemini/antigravity/brain/9f3a143b-df66-4d07-9a71-81d1cda2e72b/chilli_spice_food_1776546004893.png",
      aiHighlight: "Best value for money. Their Hakka Noodles are frequently praised in reviews.",
      actionText: "Order Now"
    },
    {
      id: 3,
      name: "The Wok",
      location: "Andheri East, Mumbai",
      budget: "$$",
      rating: "4.6",
      reviews: "2.1k",
      image: "file:///C:/Users/devan/.gemini/antigravity/brain/9f3a143b-df66-4d07-9a71-81d1cda2e72b/the_wok_food_1776546019547.png",
      aiHighlight: "Perfect for quiet dinners. Highly rated for its cozy ambiance and Manchurian.",
      actionText: "Book Table"
    }
  ];

  return (
    <main>
      <Navbar variant="results" />
      
      <div className={styles.resultsContainer}>
        <Link href="/" className={styles.backBtn}>
          <ArrowLeft size={18} />
          Back to Home
        </Link>

        <div className={styles.filtersBar}>
          <div className={styles.filterLabel}>
            <SlidersHorizontal size={16} /> Active Filters:
          </div>
          <div className={styles.activeChip}>Indo-Chinese <span>×</span></div>
          <div className={styles.activeChip}>Mumbai <span>×</span></div>
          <div className={styles.activeChip}>Budget: $$ <span>×</span></div>
        </div>

        <div className={`animate-fade-in ${styles.aiFeedbackCard}`}>
          <div className={styles.aiIcon}>
            <Sparkles size={20} />
          </div>
          <div className={styles.aiContent}>
            <h3>Curated for your Indo-Chinese Cravings</h3>
            <p>Based on your request for authentic Indo-Chinese in Mumbai within a moderate budget, I've prioritized spots known for their legendary Schezwan preparations and wok-tossed noodles. Golden Dragon leads with its heritage, while Chilli & Spice offers incredible value for casual dining.</p>
          </div>
        </div>

        <div className={styles.resultsGrid}>
          {mockResults.map((restaurant, idx) => (
            <div key={restaurant.id} className={`animate-fade-in ${styles.restaurantCard}`} style={{ animationDelay: `${idx * 0.1}s` }}>
              <div 
                className={styles.cardImage} 
                style={{ backgroundImage: `url("${restaurant.image}")` }}
              >
                <div className={styles.ratingBadge}>
                  <Star size={12} fill="var(--primary-red)" color="var(--primary-red)" />
                  {restaurant.rating} <span style={{ color: '#828282', fontWeight: 'normal' }}>({restaurant.reviews})</span>
                </div>
              </div>
              <div className={styles.cardContent}>
                <h4 className={styles.cardTitle}>{restaurant.name}</h4>
                <div className={styles.cardMeta}>
                  <MapPin size={14} /> {restaurant.location} • {restaurant.budget}
                </div>
                <div className={styles.aiHighlight}>
                  <MapPin size={14} color="var(--primary-red)" style={{ display: 'inline', marginRight: '4px', verticalAlign: 'text-bottom' }} />
                  <strong>AI Highlight: </strong> {restaurant.aiHighlight}
                </div>
                <button className={styles.cardAction}>{restaurant.actionText}</button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}
