import './globals.css'

export const metadata = {
  title: 'Zomato AI - Find Your Perfect Meal',
  description: 'AI-powered restaurant recommender',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
      </head>
      <body>{children}</body>
    </html>
  )
}
