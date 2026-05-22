export default function Modal({ title, children }) {
  return (
    <div className="modal">
      <h2>{title}</h2>
      <div className="modal-body">
        {children}
      </div>
  );
}
