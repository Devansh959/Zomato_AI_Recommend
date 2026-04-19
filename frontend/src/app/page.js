"use client";
import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { Search, Mic, MapPin } from 'lucide-react';
import Navbar from '../components/Navbar';
import styles from './page.module.css';

export default function Home() {
  const router = useRouter();
  
  // Aligning exactly with the backend UserPreferences
  const [query, setQuery] = useState(''); // Maps to additional_preferences
  const [location, setLocation] = useState('Any');
  const [cuisine, setCuisine] = useState('');
  const [maxBudget, setMaxBudget] = useState(1500);
  const [minRating, setMinRating] = useState(4.0);
  
  const [locationsList, setLocationsList] = useState(["Any"]);

  useEffect(() => {
    // Fetch locations from backend just like Streamlit did
    fetch('http://127.0.0.1:8000/api/locations')
      .then(res => res.json())
      .then(data => {
        if (data.locations) setLocationsList(data.locations);
      })
      .catch(err => console.error("Failed to fetch locations:", err));
  }, []);

  const handleSearch = (e) => {
    e.preventDefault();
    // In a real integration, we pass these to the results page or context
    const searchParams = new URLSearchParams({
      location: location !== 'Any' ? location : '',
      cuisine,
      max_budget: maxBudget,
      min_rating: minRating,
      additional_preferences: query
    });
    router.push(`/results?${searchParams.toString()}`);
  };

  const bgImageStyle = {
    backgroundImage: `url("file:///C:/Users/devan/.gemini/antigravity/brain/9f3a143b-df66-4d07-9a71-81d1cda2e72b/hero_bg_1776545679606.png")`
  };

  return (
    <main>
      <Navbar variant="home" />
      <div className={styles.heroSection}>
        <div className={styles.bgImage} style={bgImageStyle}></div>
        
        <div className={`glass-card animate-fade-in ${styles.searchContainer}`}>
          <div>
            <h1 className={styles.title}>Find Your Perfect Meal with</h1>
            <p className={styles.subtitle}>Describe what you're craving. We'll handle the rest.</p>
          </div>

          <form onSubmit={handleSearch} className={styles.searchBarWrapper}>
            <Search size={20} className={styles.searchIcon} />
            <input 
              type="text" 
              className={styles.searchInput}
              placeholder="e.g., Must have a great view, family friendly..."
              value={query}
              onChange={(e) => setQuery(e.target.value)}
            />
            <Mic size={20} className={styles.micIcon} />
            <button type="submit" className={styles.sendBtn}>Find Restaurants</button>
          </form>

          <div className={styles.chipsContainer}>
            <button className="chip" type="button" onClick={() => setCuisine("Italian")}>Italian</button>
            <button className="chip" type="button" onClick={() => setQuery(query + " Spicy")}>Spicy</button>
            <button className="chip" type="button" onClick={() => setCuisine("Cafe")}>Cafe</button>
            <button className="chip" type="button" onClick={() => setLocation("Mumbai")}><MapPin size={14} /> Mumbai</button>
          </div>

          <div className={styles.filtersGrid}>
            <div className={styles.filterGroup}>
              <span className={styles.filterLabel}>LOCATION</span>
              <select className={styles.filterSelect} value={location} onChange={e => setLocation(e.target.value)}>
                {locationsList.map(loc => (
                  <option key={loc} value={loc}>{loc}</option>
                ))}
              </select>
            </div>
            
            <div className={styles.filterGroup}>
              <span className={styles.filterLabel}>CUISINE</span>
              <input 
                type="text" 
                className={styles.filterInput} 
                placeholder="e.g., Chinese" 
                value={cuisine} 
                onChange={e => setCuisine(e.target.value)} 
              />
            </div>
            
            <div className={styles.filterGroup}>
              <span className={styles.filterLabel}>
                MAX BUDGET <span>₹{maxBudget}</span>
              </span>
              <input 
                type="range" 
                className={styles.filterSlider} 
                min="100" max="5000" step="100" 
                value={maxBudget} 
                onChange={e => setMaxBudget(Number(e.target.value))} 
              />
            </div>
            
            <div className={styles.filterGroup}>
              <span className={styles.filterLabel}>
                MIN RATING <span>{minRating}★</span>
              </span>
              <input 
                type="range" 
                className={styles.filterSlider} 
                min="1.0" max="5.0" step="0.1" 
                value={minRating} 
                onChange={e => setMinRating(Number(e.target.value))} 
              />
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}

