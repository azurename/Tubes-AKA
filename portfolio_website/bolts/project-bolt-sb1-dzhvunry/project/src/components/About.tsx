import React from 'react';
import { Code, Palette, Terminal } from 'lucide-react';

const About = () => {
  const skills = [
    {
      icon: <Code className="w-6 h-6 text-purple-400" />,
      title: "Frontend Development",
      description: "Building responsive and interactive web applications using modern frameworks"
    },
    {
      icon: <Terminal className="w-6 h-6 text-purple-400" />,
      title: "Backend Development",
      description: "Creating robust server-side applications and RESTful APIs"
    },
    {
      icon: <Palette className="w-6 h-6 text-purple-400" />,
      title: "UI/UX Design",
      description: "Designing intuitive and beautiful user interfaces with attention to detail"
    }
  ];

  return (
    <section id="about" className="py-20 bg-zinc-800">
      <div className="container mx-auto px-4">
        <div className="max-w-3xl mx-auto text-center mb-16">
          <h2 className="text-3xl font-bold text-white mb-4">About Me</h2>
          <p className="text-gray-400">
            I'm a passionate developer who loves creating beautiful and functional web applications.
            With a strong foundation in both design and development, I strive to build seamless
            digital experiences that users love.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {skills.map((skill, index) => (
            <div
              key={index}
              className="p-6 bg-zinc-900 rounded-lg hover:transform hover:-translate-y-2 transition-all duration-300"
            >
              <div className="mb-4">{skill.icon}</div>
              <h3 className="text-xl font-semibold text-white mb-2">{skill.title}</h3>
              <p className="text-gray-400">{skill.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default About;