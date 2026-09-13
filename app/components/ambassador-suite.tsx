"use client";

import { useRef, useState } from "react";

const images = [
  {
    src: "/assets/ambassador/kol-manager-01-dashboard.png",
    alt: "KOL Manager Suite ambassador dashboard",
  },
  {
    src: "/assets/ambassador/kol-manager-02-lead-dashboards.png",
    alt: "KOL Manager Suite lead dashboards",
  },
  {
    src: "/assets/ambassador/kol-manager-03-team-chat.png",
    alt: "KOL Manager Suite team conversation",
  },
];

export default function AmbassadorSuite() {
  const [active, setActive] = useState(0);
  const startX = useRef(0);

  const handlePointerDown = (event: React.PointerEvent<HTMLDivElement>) => {
    startX.current = event.clientX;
  };

  const handlePointerUp = (event: React.PointerEvent<HTMLDivElement>) => {
    const distance = event.clientX - startX.current;

    if (Math.abs(distance) > 55) {
      if (distance < 0) {
        setActive((value) => Math.min(value + 1, images.length - 1));
      } else {
        setActive((value) => Math.max(value - 1, 0));
      }
    }
  };

  return (
    <div className="ambassador-suite">
      <p className="section-label ambassador-suite-label">
        Built · Ambassador Operations
      </p>

      <div className="ambassador-suite-grid">
        <div
          className="ambassador-suite-preview"
          onPointerDown={handlePointerDown}
          onPointerUp={handlePointerUp}
          onPointerCancel={() => {}}
        >
          {images.map((image, index) => {
            const relative = index - active;

            let state = "is-hidden";

            if (relative === 0) state = "is-active";
            if (relative === 1) state = "is-next";

            return (
              <div
                className={`ambassador-suite-preview-card ${state}`}
                key={image.src}
              >
                <img src={image.src} alt={image.alt} draggable={false} />
              </div>
            );
          })}
        </div>

        <div className="ambassador-suite-copy">
          <h3 className="card-title">
            Eventually, I ended up on the other side of the program.
          </h3>

          <p className="card-tagline">
            I joined Orion as an ambassador and realised how much of the
            program was being managed through spreadsheets and a Telegram
            group. I decided to build a KOL Manager Suite around the work
            instead, giving the leads and ambassadors the tools to actually
            manage it.
          </p>

          <p className="card-tagline">
            That earned me a raise, and eventually, I ended up on the other
            side of the program as a Lead Ambassador.
          </p>

          <a
            className="campaign-link"
            href="https://github.com/nedsoft057/orion-agents"
            target="_blank"
            rel="noreferrer"
          >
            GitHub ↗
          </a>
        </div>
      </div>
    </div>
  );
}
