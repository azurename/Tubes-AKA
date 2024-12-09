import React from 'react';
import { ArrowRight } from 'lucide-react';

const Hero = () => {
  return (
    <section className="min-h-screen flex items-center justify-center pt-20 pb-16">
      <div className="container">
        <div className="max-w-3xl mx-auto text-center">
          <h1 className="text-4xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-primary to-purple-400 bg-clip-text text-transparent">
            Creative Developer
          </h1>
          <p className="text-xl text-zinc-400 mb-8">
            Building beautiful digital experiences with modern web technologies
          </p>
          <div className="flex flex-wrap justify-center gap-4">
            <a
              href="#projects"
              className="px-6 py-3 bg-primary hover:bg-primary-dark rounded-lg flex items-center gap-2 transition-colors"
            >
              View Projects
              <ArrowRight className="w-5 h-5" />
            </a>
            <a
              href="#contact"
              className="px-6 py-3 border border-primary text-primary hover:bg-primary/10 rounded-lg transition-colors"
            >
              Contact Me
            </a>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;