import React from 'react';

import './faq.scss';

const AddFaq = () => {
  const getView = (list) => {
    return list.map((faq) => {
      const linkList =
        faq.content &&
        faq.content.map((item) => {
          return (
            <a href={item.href} target={item.target} rel={item.rel}>
              <label>{item.label}</label>
            </a>
          );
        });
      return (
        <li>
          {faq.subheading && <h3>{faq.subheading}</h3>}
          {linkList}
        </li>
      );
    });
  };
  const faqList = [
    {
      subheading: 'large Data Sets',
      content: [
        {
          href: '',
          target: '_blank',
          rel: 'noopener noreferrer',
          label: 'Handling large data sets (>10M rows in last 30 days)'
        }
      ]
    },
    {
      subheading: 'Datetime Format',
      content: [
        {
          href: '',
          target: '_blank',
          rel: 'noopener noreferrer',
          label: 'Using “Cast” while handling datetime columns'
        },
        {
          href: '',
          target: '_blank',
          rel: 'noopener noreferrer',
          label: 'Handling “String” format timestamps'
        },
        {
          href: '',
          target: '_blank',
          rel: 'noopener noreferrer',
          label: 'Handling timezone aware timestamps'
        }
      ]
    },
    {
      subheading: 'Dimensions',
      content: [
        {
          href: '',
          target: '_blank',
          rel: 'noopener noreferrer',
          label: 'Using a numerical column as dimension'
        },
        {
          href: '',
          target: '_blank',
          rel: 'noopener noreferrer',
          label: 'Using high cardinality (>1000) columns as dimension'
        }
      ]
    }
  ];

  const videoTutorialList = [
    {
      content: [
        {
          href: '',
          target: '_blank',
          rel: 'noopener noreferrer',
          label: 'Creating your first KPI'
        }
      ]
    }
  ];

  const videoTutorialView = getView(videoTutorialList);

  const faqView = getView(faqList);

  return (
    <div className="faq-section">
      <div className="faq__wrapper-content">
        <div className="faq__title">
          <h2>FAQs</h2>
        </div>
        <ul className="faq__separate_links">{faqView}</ul>
      </div>
      <div className="faq__wrapper-content">
        <div className="faq__title">
          <h2>Video tutorials</h2>
        </div>
        <ul className="faq__separate_links">{videoTutorialView}</ul>
      </div>
      <div className="faq__support-content">
        <p>
          Need help? Feel free to join our community Slack and ping us there!
        </p>
      </div>
    </div>
  );
};
export default AddFaq;
